from tkinter import Tk, Text, messagebox, StringVar
from tkinter.messagebox import showinfo, showwarning
from tkinter.ttk import Label, Entry, Button, LabelFrame
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']
rcParams['figure.autolayout'] = True

def calc():
    try:
        names, data = get_data()
        gr = GR(data, float(alpha.get()))
        text2.delete('1.0','end')
        text2.insert('insert', ','.join([str(i) for i in gr]))
        if max([len(name) for name in names]) > 5: r = 45
        else: r = 0
        drawPic(gr, names, r)
    except:
        warn()

def reset():
    workspace_path.set('')
    text1.delete('1.0','end')
    text2.delete('1.0','end')
    alpha.delete(0, 'end')
    alpha.insert(0, 0.5)
    figure1.clf(); draw_canvas.draw()

def warn():
    showwarning('警告', '请先输入数据或检查数据格式是否符合要求！！！')

def load_csv():
    filename = askopenfilename(filetypes=[('csv files','.csv'),
                                          ('all files','.*')])
    if filename != '':
        workspace_path.set(filename)
        f0 = open(filename, 'r')
        text1.delete('1.0','end')
        text1.insert('insert', f0.read())
        f0.close()
    else:
        showinfo('提示', '您没有选择任何文件!')

def save_fig():
    pass
        
def get_data():
    f1 = text1.get('1.0', 'end').replace('\t', ',')
    f1 = f1.strip('\n\r').split('\n')
    f2 = [item.split(',') for item in f1]
    names = [i[0] for i in f2[2:]]
    data = [[float(j) for j in i[1:]] for i in f2[1:]]
    return names, data

def GR(data, alpha):
    '''data:(row, col)
    [[y1, y2, y3, y4, y5],
    [x11, x12, x13, x14, x15],
    ...
    [x51, x52, x53, x54, x55]]
    '''
    
    col = len(data[0])
    std = [[c / r[0] if r[0] != 0 else c / (r[0] + 0.000000001) for c in r] for r in data]
    diff = [[abs(y - x) for y, x in zip(std[0], r)] for r in std[1:]]
    flatten = [c for r in diff for c in r]
    minmum = min(flatten)
    maxmum = max(flatten)
    coef = [[(minmum + maxmum * alpha) / (c + maxmum * alpha)
               for c in r] for r in diff]
    relation = [round(sum(r) / col, 3) for r in coef]
    return relation

def drawPic(gr, names, r):
    #清空图像，以使得前后两次绘制的图像不会重叠
    figure1.clf()
    draw = figure1.add_subplot(111)
    draw.plot(gr, color='green', marker='o')
    for i, j in zip(gr, range(len(names))):
        draw.text(j, i, str(i),
                  horizontalalignment='center',
                  verticalalignment='top')
    #drawPic.a.set_ylim(0.0, 1.0)
    draw.set_title('灰色关联度')
    draw.set_xticks(range(len(names)))
    draw.set_xticklabels(names, rotation=r)
    draw.set_xlabel('指标')
    draw.set_ylabel('关联系数')
    draw_canvas.draw()
    
root = Tk()
root.title('GreyRelational')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
win_width, win_height = 750, 800
x = (screen_width - win_width) / 2
y = (screen_height - win_height) / 2
root.geometry('%dx%d+%d+%d' %(win_width, win_height, x, y))
root.resizable(0,0)

lb1 = LabelFrame(root, width=600, height=800, text='数据输入')
lb1.grid(row=0, column=0, padx=10)

workspace_path = StringVar(root)
workspace_label = Label(lb1, text='文件路径:')
workspace_label.grid(row=0, column=0, sticky='W')
entry_workspace = Entry(lb1, textvariable=workspace_path, width=80)
entry_workspace.grid(row=0, column=1, sticky='W')
button_workspace_path = Button(lb1, text='浏览',command=load_csv)
button_workspace_path.grid(row=0,column=2, sticky='W')

text1 = ScrolledText(lb1, width=100, height=20)
text1.grid(row=1, column=0, columnspan=3)
text1.update()

lb2 = LabelFrame(root, width=300, height=600, text='参数输入，计算和结果输出')
lb2.grid(row=1, column=0, sticky='W', padx=10)

Label(lb2, text='系数').grid(row=0, column=0)

alpha = Entry(lb2)
alpha.insert(0, 0.5)
btn1 = Button(lb2, text="灰色关联度", command=calc)
btn2 = Button(lb2, text="重置", command=reset)

alpha.grid(row=0, column=1)
btn1.grid(row=0, column=2, padx=10)
btn2.grid(row=0, column=3)

lb3 = LabelFrame(root, width=300, height=600, text='结果输出')
lb3.grid(row=2, column=0, padx=10)

text2 = ScrolledText(lb3, width=42, height=30, background='#ffffff')
text2.grid(row=0, column=0)
text2.update()
text2.bind('<KeyPress>', lambda e: 'break' )

figure1 = Figure(figsize=(4, 4), dpi=100)
draw_canvas = FigureCanvasTkAgg(figure1, master=lb3)
draw_canvas.get_tk_widget().grid(row=0, column=1)

root.mainloop()


from sklearn.metrics import roc_curve, auc
import pylab as plt
import warnings
warnings.filterwarnings('ignore')

f = open('data.csv', 'r')
data = [i.strip().split(',') for i in f.readlines()[1:]]
y_true = [float(i[0]) for i in data]
y_pred = [float(i[1]) for i in data]
f.close()
del data

fpr, tpr, threshold = roc_curve(y_true, y_pred)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(8, 6))
plt.title('ROC')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.3f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.savefig('roc.png', dpi=300)
plt.show()
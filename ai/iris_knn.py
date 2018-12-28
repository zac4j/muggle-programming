import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

DATA_FILE = './data/Iris.csv'

SPECIES = {
    'Iris-setosa': 0,  # 山鸢尾
    'Iris-versicolor': 1,  # 变色鸢尾
    'Iris-virginica': 2  # 维吉尼亚鸢尾
}

# 使用的特征列
FEAT_COLS = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']


def main():
    iris_data = pd.read_csv(DATA_FILE, index_col='Id')
    iris_data['Label'] = iris_data['Species'].map(SPECIES)

    # 获取数据集特征
    x = iris_data[FEAT_COLS].values

    # 获取数据标签
    y = iris_data['Label'].values

    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1 / 3, random_state=10)

    # 声明模型
    knn_model = KNeighborsClassifier()

    # 训练模型
    knn_model.fit(x_train, y_train)

    # 评价模型
    accuracy = knn_model.score(x_test, y_test)
    print('预测准确率：{:.2f}%'.format(accuracy * 100))

    # 获取单个测试样本
    idx = 10
    test_sample_feat = [x_test[idx, :]]
    y_true = y_test[idx]
    y_pred = knn_model.predict(test_sample_feat)
    print('真实标签{}, 预测标签{}'.format(y_true, y_pred))


if __name__ == '__main__':
    main()

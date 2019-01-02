import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from ai import ai_utils

DATA_FILE = './data/Iris.csv'

SPECIES = {
    'Iris-setosa': 0,  # 山鸢尾
    'Iris-versicolor': 1,  # 变色鸢尾
    'Iris-virginica': 2  # 维吉尼亚鸢尾
}

# 使用的特征列
FEAT_COLS = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']


def evaluate_knn(iris_data, sel_cols, k_val):
    x = iris_data[sel_cols].values
    y = iris_data['Label'].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1 / 3, random_state=10)

    knn_model = KNeighborsClassifier(n_neighbors=k_val)
    knn_model.fit(x_train, y_train)
    accuracy = knn_model.score(x_test, y_test)
    print('k={}, accuracy={:.2f}%'.format(k_val, accuracy * 100))

    ai_utils.plot_knn_boundary(knn_model, x_test, y_test, 'Sepal Length vs Sepal Width, k={}'.format(k_val),
                               save_fig='sepal_k{}.png'.format(k_val))


def main():
    # 读取数据集
    iris_data = pd.read_csv(DATA_FILE, index_col='Id')
    iris_data['Label'] = iris_data['Species'].map(SPECIES)

    k_vals = [3, 5, 10]
    sel_cols = ['SepalLengthCm', 'SepalWidthCm']
    for k_val in k_vals:
        evaluate_knn(iris_data, sel_cols, k_val)


if __name__ == '__main__':
    main()

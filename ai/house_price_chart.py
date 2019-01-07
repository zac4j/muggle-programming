import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

DATA_FILE = './data/house_data.csv'

# 使用特征列
FEAT_COLS = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement']


def plot_fitting_line(linear_reg_model, x, y, feat):
    w = linear_reg_model.coef_
    b = linear_reg_model.intercept_

    plt.figure()
    # 样本点
    plt.scatter(x, y, alpha=0.5)
    # 直线
    plt.plot(x, w * x + b, c='red')
    plt.title(feat)
    plt.show()


def main():
    house_data = pd.read_csv(DATA_FILE, usecols=FEAT_COLS + ['price'])

    for feat in FEAT_COLS:
        # 转换行向量
        x = house_data[feat].values.reshape(-1, 1)
        y = house_data['price'].values

        # 分割数据集
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1 / 3, random_state=10)
        # 建立线性回归模型
        linear_reg_model = LinearRegression()
        # 模型训练
        linear_reg_model.fit(x_train, y_train)
        # 验证模型
        r2_score = linear_reg_model.score(x_test, y_test)
        print('特征：{}, 模型的R2值:{}'.format(feat, r2_score))

        # 绘制拟合图形
        plot_fitting_line(linear_reg_model, x_test, y_test, feat)


if __name__ == '__main__':
    main()

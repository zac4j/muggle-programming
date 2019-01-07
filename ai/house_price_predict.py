import pandas as pd
from ai import ai_utils
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

DATA_FILE = './data/house_data.csv'

# 使用特征列
FEAT_COLS = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement']


def main():
    house_data = pd.read_csv(DATA_FILE, usecols=FEAT_COLS + ['price'])
    ai_utils.plot_feat_and_price(house_data)

    x = house_data[FEAT_COLS].values
    y = house_data['price'].values

    # 分割数据集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1 / 3, random_state=10)

    # 建立线性回归模型
    linear_reg_model = LinearRegression()
    # 模型训练
    linear_reg_model.fit(x_train, y_train)
    # 验证模型
    r2_score = linear_reg_model.score(x_test, y_test)
    print('模型的R2值', r2_score)

    # 单个样本房价预测
    i = 50
    single_test_feat = x_test[i, :]
    y_reality = y_test[i]
    y_predict = linear_reg_model.predict([single_test_feat])
    print("样本特征：", single_test_feat)
    print("真实价格: {}, 预测价格: {}".format(y_reality, y_predict))


if __name__ == '__main__':
    main()

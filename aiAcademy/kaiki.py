from sklearn.linear_model import LinearRegression
x = [[12,2],[16,1],[20,0],[28,2],[36,0]]
y = [[700],[900],[1300],[1750],[1800]]

model= LinearRegression()
model.fit(x,y)

x_test = [[16,2],[18,0],[22,2],[32,2],[24,0]]
y_test = [[1100],[850],[1500],[1800],[1100]]

prices = model.predict(x_test)
for i, price in enumerate(prices):
    print('Predicated:%s, Target:%s' %(price, y_test[i]))

score = model.score(x_test, y_test)
print('r-squared:', score)
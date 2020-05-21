import pickle
bal = 0.00

loan = 0.00

with open('store.pkl', 'wb') as f:
    pickle.dump([bal, loan], f)

print('Success')

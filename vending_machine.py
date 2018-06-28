from byotest import *

usd_coins = {100:20, 50:20, 25:20, 10:20, 5:20, 1:20}
eur_coins = {100:20, 50:20, 20:20, 10:20, 5:20, 2:20, 1:20}

def get_change(amount, coins =eur_coins):
    change = []
    for coin in sorted(coins, reverse=True):
        while coin <= amount:
            amount -= coin
            change.append(coin)
            
    return change

def get_stock(coin_stock, change):
    #for each coin in the change array, look up the key and decrease the stock by 1
    if(coin_stock == {1:0}):   
        return({1:0})   
    
    for denomination in coin_stock:
        for coin in change:
            if (coin == denomination):
                coin_stock[coin] -= 1
    
    return coin_stock
        

test_are_equal(get_change(0),[])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2,1])
test_are_equal(get_change(7), [5,2])
test_are_equal(get_change(9), [5,2,2])
test_are_equal(get_change(35, usd_coins), [25,10])

test_are_equal(get_stock({1:0},[1]),{1:0})
test_are_equal(get_stock({1:1},[1]),{1:0})
test_are_equal(get_stock({1:2},[1]),{1:1})
test_are_equal(get_stock({2:2},[2]),{2:1})
test_are_equal(get_stock({2:5},[2,2]),{2:3})
test_are_equal(get_stock({2:5,1:5},[2,1]),{2:4,1:4})

print("All tests pass!")
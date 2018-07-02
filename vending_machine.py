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
    
#what do take each coin from the change array and decrease the stock of that coin by one in the stock dictionary
#for each coin in the coin list, go through the stock dictionary, find the coin and decrease the stock by 1 while the stock > 0
#change requires 2 x 5's. when the coin in the coin stock is equal to 5, decrease stock by 1 while stock is greater than 0
#for each coin in the change, look up the dictionary key, and decrease the stock by 1 while it is bigger than zero

    for coin in change:
        #while the coin stock is greater than zero, decrease the stock by 1. 
        if (coin_stock[coin] > 0):
            coin_stock[coin] -= 1
        #if the coin stock is zero then for keys less than the coin value loop through and decreasing the stock while it is less than zero
        #test_are_equal(get_stock({2:0,1:2},[2]),{2:0,1:0})
        #else for the coin_stockitems < coin:
            #while 
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
test_are_equal(get_stock({2:5,1:5, 50:3, 100:1},[100,50,50,2,1]),{2:4,1:4,50:1, 100:0})
test_are_equal(get_stock({2:0,1:0, 50:0, 100:0},[100,50,50,2,1]),{2:0,1:0, 50:0, 100:0})
test_are_equal(get_stock({2:0,1:2},[2]),{2:0,1:0})

print("All tests pass!")
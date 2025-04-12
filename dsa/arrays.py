def main():
    
    expns: list[int] = [2200, 2350, 2600, 2500, 2100]
    # 1. In Feb, how many dollars you spent extra compare to January?
    add_expns = expns[1] - expns[0]
    print(add_expns)
    
    # 2. Find out your total expense in first quarter (first three months) of the year.
    quar_expns = expns[0] + expns[1] + expns[3]
    print(quar_expns)
    
    # 3. Find out if you spent exactly 2000 dollars in any month
    spent = []
    for expense in expns:
        if expense == 2000: 
            spent.append(True)
        spent.append(False)
    print(spent)
    
    # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    expns.append(1980)
    
    # 5. You returned an item that you bought in a month of April and
    # got a refund of 200$. Make a correction to your monthly expense list
    # based on this
    
    expns[3] = expns[3] - 200
    print(expns)


if __name__ == "__main__":
    main()
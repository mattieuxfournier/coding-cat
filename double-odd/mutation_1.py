def double_odd(i_list):
    '''
    mutation

    ''' 
    new_list = []
        for i in range(1, len(i_list), 2):
            if i_list[i] % 2 != 0:
                new_list.append(i_list[i])
    return new_list

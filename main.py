def created_ab_group(n_customers: int, n_first_id: int = 0) -> dict():
    # возвращает словарь в виде (id группы: число покупателей в группе)
    dict_result = {}
    for customer_id in range(n_first_id, n_customers):
        if customer_id % 10 != 0:
            sm += 1
        else:
            sm = sum(map(int, str(customer_id)))
        if sm in dict_result:
            dict_result[sm] += 1
        else:
            dict_result[sm] = 1
    return dict_result



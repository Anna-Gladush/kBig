def kbig(nums, k):
    if k < 2:
        return max(nums)

    else:
        count_numb_in_nums = 1  # Введем начальную длину
        for _ in range(1, len(nums)):
            if count_numb_in_nums == k:
                break

            nums.remove(max(nums)) #удаляем самый большой элемент из списка
            count_numb_in_nums += 1

        return max(nums)


print(kbig(nums, k))

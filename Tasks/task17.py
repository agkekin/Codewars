def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    my_time = pontoon_distance / you_speed
    shark_time = shark_distance / shark_speed
    print('my_time',my_time,'shark_time',shark_time )

    if dolphin:
        shark_time = shark_time * 2
        print('shark_time_new', shark_time)
    if my_time < shark_time:
        print('Alive!')
        return 'Alive!'
    else:
        print('Shark Bait!')
        return 'Shark Bait!'


if __name__ == '__main__':
    assert shark(12, 50, 4, 8, True) == 'Alive!'
    assert shark(7, 55, 4, 16, True) == 'Alive!'
    assert shark(24, 0, 4, 8, True) == 'Shark Bait!'

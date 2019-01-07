import cProfile


profiler = cProfile.Profile()
profiler.disable()


def main():
    profiler.enable()
    print('hello world')
    profiler.disable()


if __name__ == '__main__':
    main()
    profiler.print_stats(sort='cumtime')

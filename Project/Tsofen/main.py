from compare_source_target import CompareSourceTarget

if __name__ == '__main__':
    try:
        CompareClass = CompareSourceTarget()
        print(CompareClass.run('json_file.json'))
        exit(0)
    except Exception as e:
        print(f"proccess failed with the following error: {e}")
        exit(1)

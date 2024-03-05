from compare_source_target import CompareSourceTarget

if __name__ == '__main__':
    try:
        CompareClass = CompareSourceTarget()
        email_addresses = 'ahmadaw@post.bgu.ac.il,briq@post.bgu.ac.il'
        print(CompareClass.run(email_addresses, 'json_file.json'))
        exit(0)
    except Exception as e:
        print(f"proccess failed with the following error: {e}")
        exit(1)

from compare_source_target import CompareSourceTarget

if __name__ == '__main__':
    try:
        email_addresses = 'ahmadaw@post.bgu.ac.il,briq@post.bgu.ac.il'
        version_file_name='json_file.json'
        CompareClass = CompareSourceTarget(email_addresses=email_addresses, version_file_name=version_file_name)
        print(CompareClass.run())
        exit(0)
    except Exception as e:
        print(f"proccess failed with the following error: {e}")
        exit(1)

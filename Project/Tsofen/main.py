from compare_source_target import CompareSourceTarget

if __name__ == '__main__':
    try:
        # These parameters are sent from user. can also be sent as paramsters to the python file.
        addresses_to_send_report = 'ahmadaw@post.bgu.ac.il,briq@post.bgu.ac.il'
        version_file_name='json_file.json'
        send_email=True
        ###############################################################

        CompareClass = CompareSourceTarget(email_addresses=addresses_to_send_report, 
                                           version_file_name=version_file_name,
                                           send_email=send_email)
        print(CompareClass.run())
        exit(0)
    except Exception as e:
        print(f"proccess failed with the following error: {e}")
        exit(1)

import unittest
from enums import Status
from compare_source_target import CompareSourceTarget

class TestCompareSourceTarget(unittest.TestCase):
    def test_validEmails_equalVersions(self):
        """
        test case to check run with valid emails and equal versions
        """
        # These parameters are sent from user. can also be sent as paramsters to the python file.
        self.addresses_to_send_report = '......@post.bgu.ac.il,.........@post.bgu.ac.il'
        self.version_file_name='json_file.json'
        self.send_email=True
        ###############################################################

        self.CompareClass = CompareSourceTarget(email_addresses=self.addresses_to_send_report, 
                                           version_file_name=self.version_file_name,
                                           send_email=self.send_email)
        self.assertEqual(self.CompareClass.run(),Status.Success.value)

    def test_validEmails_unequalVersions(self):
        """
        test case to check run with valid emails and unequal versions
        """
        self.addresses_to_send_report = '..........@post.bgu.ac.il,...........@post.bgu.ac.il'
        self.version_file_name='unequal_versions.json'
        self.send_email=True
        self.CompareClass = CompareSourceTarget(email_addresses=self.addresses_to_send_report, 
                                           version_file_name=self.version_file_name,
                                           send_email=self.send_email)
        self.assertEqual(self.CompareClass.run(),Status.Failure.value)

    def test_invalidEmails_equalVersions(self):
        """
        test case to check run with invalid emails and equal versions
        """
        self.addresses_to_send_report = 'ahmadaw.post.bgu.ac.il,briq.post.bgu.ac.il'
        self.version_file_name='json_file.json'
        self.send_email=True
        self.CompareClass = CompareSourceTarget(email_addresses=self.addresses_to_send_report, 
                                           version_file_name=self.version_file_name,
                                           send_email=self.send_email)
        with self.assertRaises(Exception):
            self.CompareClass.run()   
    
    def test_invalidEmails_unequalVersions(self):
        """
        test case to check run with invalid emails and unequal versions
        """
        self.addresses_to_send_report = 'ahmadaw.post.bgu.ac.il,briq.post.bgu.ac.il'
        self.version_file_name='unequal_versions.json'
        self.send_email=True
        self.CompareClass = CompareSourceTarget(email_addresses=self.addresses_to_send_report, 
                                           version_file_name=self.version_file_name,
                                           send_email=self.send_email)
        with self.assertRaises(Exception):
            self.CompareClass.run()  
    
    def test_validEmails_badVersionFormat(self):
        """
        test case to check run with valid emails and bad version format
        """
        self.addresses_to_send_report = '.........@post.bgu.ac.il,......@post.bgu.ac.il'
        self.version_file_name='bad_version_format.json'
        self.send_email=True
        self.CompareClass = CompareSourceTarget(email_addresses=self.addresses_to_send_report, 
                                           version_file_name=self.version_file_name,
                                           send_email=self.send_email)
        with self.assertRaises(Exception):
            self.CompareClass.run()
    
    def test_invalidEmails_badVersionFormat(self):
        """
        test case to check run with invalid emails and bad version format
        """
        self.addresses_to_send_report = 'ahmadaw.post.bgu.ac.il,briq.post.bgu.ac.il'
        self.version_file_name='bad_version_format.json'
        self.send_email=True
        self.CompareClass = CompareSourceTarget(email_addresses=self.addresses_to_send_report, 
                                           version_file_name=self.version_file_name,
                                           send_email=self.send_email)
        with self.assertRaises(Exception):
            self.CompareClass.run()

if __name__ == '__main__':
    unittest.main()
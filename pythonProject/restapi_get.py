import pyats
from pyats import aetest
import requests


class CricketPlayerInfoTest(aetest.Testcase):

    @aetest.setup
    def setup(self):
        # Load the testbed
        self.tb = self.parent.parameters['testbed']

    @aetest.test
    def test_get_cricket_players_info(self):
        # Define the API URL
        api_url = "https://api.example.com/cricket/players"

        try:
            # Make the GET request
            response = requests.get(api_url)

            # Check the response status code
            if response.status_code == 200:
                self.passed("API request successful")
                players_info = response.json()
                # Process the players_info JSON as needed
            else:
                self.failed(f"API request failed with status code: {response.status_code}")
        except Exception as e:
            self.failed(f"Error making API request: {str(e)}")


if __name__ == "__main__":
    pyats.aetest.main()

#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Wdang, 2020-Mar-22, Completed TODOs
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC
import ProcessingClasses as PC

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """

        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.

        Returns:
            None.

        """

        # TODOne modify method to accept a list of file names.
        file_name_CD, file_name_track = file_name
        with open(file_name_CD, 'w') as file:
            for cd in lst_Inventory:
                file.write(cd.get_CD_record())
        # TODOne add code to save track data to file
        with open(file_name_track, 'w') as file:
            for cd in lst_Inventory:
                tracks = cd.cd_tracks
                cd_id = cd.cd_id
                for track in tracks:
                    if track is not None:
                        record = '{},{}'.format(cd_id,track.get_track_record())
                        file.write(record)

    @staticmethod
    def load_inventory(file_name: list) -> list:
        """

        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.

        Returns:
            list: list of CD objects and its track details.

        """
        file_name_CD, file_name_track = file_name
        lst_Inventory = []
        # TODOne modify method to accept a list of file names
        try:
            with open(file_name_CD, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = DC.CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
            # TODOne add code to load track data
            with open(file_name_track, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    cd = PC.DataProcessor.select_cd(lst_Inventory, data[0])
                    track = DC.Track(data[1], data[2], data[3])
                    cd.add_track(track)

        except Exception as e:
            print('There was a general error! Make sure files to be loaded exsit!', e, e.__doc__, type(e), sep='\n')
        return lst_Inventory

class ScreenIO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Main Menu\n\n[l] load Inventory from file\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[r] Remove CD / Album\n[s] Save Inventory to file\n[x] exit\n')


    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 'r', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, r, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice


    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.

        Returns:
            None.
        """

        print('CD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] exit to Main Menu')


    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x

        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice


    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of CDs): list of CDs that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in table:
            print(cd)
        print('======================================')


    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album

        Args:
            cd (CD): CD object.

        Returns:
            None.

        """
        print('====== Current CD / Album: ======')
        print(cd)
        print('===== Track / Title / Length:====')
        print(cd.get_tracks())
        print('=================================')


    @staticmethod
    def get_track_info(table):
        """function to request Track information from User to add Track to CD / Album

        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.

        """

        trkId = ScreenIO.get_new_track_position(table)
        trkTitle = input('What is the Track\'s title? ').strip()
        trkLength = input('What is the Track\'s length? ').strip()
        return trkId, trkTitle, trkLength


    @staticmethod
    def get_new_track_position(table):
        """ Gets a new, unused track position from the user

        Args:
            table (list of CD objects): CDInventory

        Returns:
            track_id (int): New unused track position specified by the user
        
        """
        used_ids = []
        for cd in table:
            for track in cd.cd_tracks:
                if track is not None:
                    used_ids.append(track.position)

        while True:
            track_id = ScreenIO.get_typed_input('Enter a numerical Position: ', 'The entered Position is not an integer. Please enter a number')
            if track_id in used_ids:
                print("Track Position '{}' already exsits, use a different Position.\n".format(track_id))
            else:
                return track_id


    @staticmethod
    def confirm_rmv_track_position(table):
        """ confirm track position exist to be removed by user

        Args:
            table (list of CD objects): CDInventory

        Returns:
            track_id (int): New unused track position specified by the user
        
        """
        used_ids = []
        for cd in table:
            for track in cd.cd_tracks:
                if track is not None:
                    used_ids.append(track.position)

        while True:
            track_id = ScreenIO.get_typed_input('Enter a numerical Position: ', 'The entered Position is not an integer. Please enter a number')
            if track_id in used_ids:
                return track_id
            else:
                print("Track Position '{}' doesn't exsits, use a different Position.\n".format(track_id))


    @staticmethod
    def get_cd_info(table):
        """Collect user inputs to add new CDs to inventory

        Args:
            None.

        Returns:
            cd_id (int): ID for the new CD
            cd_title (string): Title for the new CD
            cd_artist (string): Artist of the new CD

        """
        
        cd_id = ScreenIO.get_new_cd_id(table)
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        return cd_id, cd_title, cd_artist


    @staticmethod
    def get_new_cd_id(table):
        """ Gets a new, unused CD ID from the user

        Args:
            table (list of CD objects): CDInventory

        Returns:
            cd_id (int): New unused CD ID specified by the user
        
        """
        used_ids = []
        for cd in table:
            used_ids.append(cd.cd_id)
        
        while True:
            cd_id = ScreenIO.get_typed_input('Enter a numerical ID: ', 'The entered ID is not an integer. Please enter a number')
            if cd_id in used_ids:
                print("CD ID '{}' already exsits, use a different ID\n".format(cd_id))
            else:
                return cd_id


    @staticmethod
    def get_typed_input(input_message, error_message):
        """Prompts the user for input and checks for the correct type.

        Prompts the user for input value of the int type displaying input_message.
        Checks for correct input type, looping until a proper type is entered
        and displays the passed error_message if bad input is passed.

        Args:
            input_message (string): Message displayed to the user prompting for input
            error_message (string): Error message displayed to the user if an incorrect type is entered

        Returns:
            typed_value (int): Int value entered by the user
        
        """

        while True:
            try:
                typed_value = int(input(input_message).strip())
                return typed_value
            except ValueError:
                print(error_message)

#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Wdang, 2020-Mar-22, Completed TODOs
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.

        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        cdId = int(cdId)
        row = DC.CD(cdId, title, artist)
        table.append(row)


    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        # TODOne add code as required

        for cd in table:
            if int(cd.cd_id) == int(cd_idx):
                return cd
        print('Could not find this CD!\n')        


    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd
        
        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """

        # TODOne add code as required
        trkID, trkTitle, trkLength = track_info
        try:
            trkID = int(trkID)
        except:
            print('Position must be an Integer')
        
        track = DC.Track(track_info[0],track_info[1],track_info[2])
        cd.add_track(track)


    @staticmethod
    def rmv_cd(IDDel, table):
        """delete a CD object based on user inputs CD ID

        Args:
            IDDel: user input CD ID for the CD to be deleted
            table: current list of CD objects in memory
            
        Returns:    
            the new list of CD objects
        """

        intRowNr = -1
        blnCDRemoved = False
        for cd in table:
            intRowNr += 1
            if int(cd.cd_id) == IDDel:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

        return table


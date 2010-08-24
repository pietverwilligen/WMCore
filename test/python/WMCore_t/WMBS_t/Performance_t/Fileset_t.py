#!/usr/bin/env python

import logging, random
from WMCore_t.WMBS_t.Performance_t.WMBSBase import WMBSBase
from WMCore.WMBS.Fileset import Fileset
from WMCore.WMBS.File import File
from WMCore.Database.DBFactory import DBFactory

class FilesetTest(WMBSBase):
    """
    __FilesetTest__

     Performance testcase for WMBS Fileset class

     This class is abstract, proceed to the DB specific testcase
     to run the test


    """
    def setUp(self, sqlURI='', logarg=''):
        #Call common setUp method from WMBSBase
                
        self.logger = logging.getLogger(logarg + 'FilesetPerformanceTest')
        
        dbf = DBFactory(self.logger, sqlURI)
        
        WMBSBase.setUp(self,dbf=dbf)

    def tearDown(self):
        #Call superclass tearDown method
        WMBSBase.tearDown(self)

    def testNew(self):
        print "testNew"
        
        testname = 'TestFileset1234'

        time = self.perfTest(dao=self.dao, action='Fileset.New', name=testname)
        assert time <= self.threshold, 'New DAO class - Operation too slow ( elapsed time:'+str(time)+', threshold:'+str(self.threshold)+' )'   

    def testDelete(self):
        print "testDelete"

        time = self.perfTest(dao=self.dao, action='Fileset.Delete', name=self.testFileset.name)
        assert time <= self.threshold, 'Delete DAO class - Operation too slow ( elapsed time:'+str(time)+', threshold:'+str(self.threshold)+' )'   

    def testExists(self):
        print "testExists"

        time = self.perfTest(dao=self.dao, action='Fileset.Exists', name=self.testFileset.name)
        assert time <= self.threshold, 'Exists DAO class - Operation too slow ( elapsed time:'+str(time)+', threshold:'+str(self.threshold)+' )'   

    def testLoadFromID(self):
        print "testLoadFromID"

        time = self.perfTest(dao=self.dao, action='Fileset.LoadFromID', fileset=self.testFileset.id)
        assert time <= self.threshold, 'LoadFromID DAO class - Operation too slow ( elapsed time:'+str(time)+', threshold:'+str(self.threshold)+' )'  

    def testLoadFromName(self):
        print "testLoadFromName"

        time = self.perfTest(dao=self.dao, action='Fileset.LoadFromName', fileset=self.testFileset.name)
        assert time <= self.threshold, 'LoadFromName DAO class - Operation too slow ( elapsed time:'+str(time)+', threshold:'+str(self.threshold)+' )'

    #Waiting for fileset parentage to be needed 

#    def testParentage(self):
#        print "testParentage"

#        childname = "ChildFileset1234"

#        childFileset = Fileset(name=childname,                         
#                        logger=self.logger, 
#                        dbfactory=self.dbf) 
#        childFileset.create()

        #Add the child fileset to the DB
        #self.dao(classname='Fileset.New').execute(name=childname)
        

#        time = self.perfTest(dao=self.dao, action='Fileset.Parentage', parent=childname, child=self.testFileset.name)
#        assert time <= self.threshold, 'Parentage DAO class - Operation too slow ( elapsed time:'+str(time)+', threshold:'+str(self.threshold)+' )'


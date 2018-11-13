# CISI collection

UNIX formatted version of the CISI collection
                                                      
## 18 Editions of the Dewey Decimal Classifications                
   
The present study is a history of the DEWEY Decimal          
Classification.  The first edition of the DDC was published
in 1876, the eighteenth edition in 1971, and future editions
will continue to appear as needed.  In spite of the DDC's
long and healthy life, however, its full story has never
been told.  

There have been biographies of Dewey
that briefly describe his system, but this is the first
attempt to provide a detailed history of the work that
more than any other has spurred the growth of
librarianship in this country and abroad.

This project is realized for Rennes 1 University's Big data Master program's "Data Indexisation and Visualisation Cursus".
One of the main goal of this projets is to improve searching algorithme.

### Evaluation programme for TREC formatted input

Once downloaded evaluation.pl, put execution rights 

chmod u+x evaluation.pl

### To use it:
evaluation.pl -results my_result_file.res -relevance cisi.rel

result file format:

  
| num_query | 'Q0' | id_document | rank | score | 'Exp' |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 1  | Q0  | 38  | 1 | 23.5217647552  | Exp  |
| 1  | Q0  | 52  | 2 | 23.1733417511  | Exp  |
| 1  | Q0  | 52  | 3 | 23.036365509   | Exp  |
| 1  | Q0  | 52  | 4 | 22.7806720734  | Exp  |



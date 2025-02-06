import csv
import io
import shutil

# https://docs.python.org/3/library/csv.html#csv.Dialect
# excel-tab

# My Project cogeco-01-002-uat-00021

def open_tsv(filename):
  
  f_ = io.StringIO()
  
  with open(filename, "r") as f:
    
    filecopy = shutil.copyfileobj(f, f_)
    
    # Return to position 0 after the copy
    f_.seek(0)
    
    # TSV Reader to Dict object
    google_sheets_tsv_export = csv.excel_tab()
    reader = csv.DictReader(f_, dialect=google_sheets_tsv_export)
  
    return reader
    

if __name__ == "__main__":
  
  # import sys
  #
  # filename = sys.argv[1]
  #
  # t = open_tsv(filename)
  #
  # rows = [r for r in t]
  #
  # print("file:\t{}\nfields:\t{}".format(filename, t.fieldnames))
  
  import glob
    
    
  # Fields from the 1st row
  for f in glob.glob("./*.tsv"):
    
    t = open_tsv(f)
    print("file:\t{}\nfields:\t{}\n  ".format(f, t.fieldnames))
    
  
  # Samples
  import pprint
  for f in glob.glob("./*.tsv"):
    
    t = open_tsv(f)

    rows = [r for r in t]

    print("### SAMPLE {}\n\n".format(f))

    for r in range(0, 2):
      if r < len(rows):
        pprint.pprint(rows[r])
    
    print("###\n\n")
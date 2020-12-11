import pandas

tables = pandas.read_excel ('https://www.eia.gov/dnav/pet/hist_xls/EMD_EPD2D_PTE_R50_DPGw.xls', sheet_name='Data 1',
                            header = 2, index_col='Date')

print(tables)

ill add to this soon . i need help for sure

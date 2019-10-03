#pa
import os
import cdsapi

lagringspath = '/uio/lagringshotell/geofag/students/metos/stinsage/era5_files/'

def download_single_layer_file(var, years_subset):
    c = cdsapi.Client()
    filename = lagringspath + "{}_ERA5_{}0401-{}0930.nc".format(var, years_subset[0], years_subset[-1])
    c.retrieve(
        'reanalysis-era5-single-levels',
        {   'product_type':'reanalysis',
            'area'    : '75/-25/30/45', # North, West, South, East. Default: global
            'grid'    : '0.25/0.25', # Latitude/longitude grid: east-west (longitude) and north-south resolution (latitude). Default: reduced Gaussian grid
            'format':'netcdf',
            'variable':var,
            'year':years_subset,
            'month':[
                '04','05','06','07','08','09'
                
            
            ],
            'day':[
                '01','02','03',
                '04','05','06',
                '07','08','09',
                '10','11','12',
                '13','14','15',
                '16','17','18',
                '19','20','21',
                '22','23','24',
                '25','26','27',
                '28','29','30',
                '31'
            ],
            'time':[
                '00:00','01:00','02:00',
                '03:00','04:00','05:00',
                '06:00','07:00','08:00',
                '09:00','10:00','11:00',
                '12:00','13:00','14:00',
                '15:00','16:00','17:00',
                '18:00','19:00','20:00',
                '21:00','22:00','23:00'
            ]
        },
        filename)
def download_pressure_layer_file(var, level, years_subset):
    c = cdsapi.Client()
    filename = lagringspath + "{}_ERA5_{}0401-{}0930.nc".format(var, years_subset[0], years_subset[-1])
    c.retrieve(
        'reanalysis-era5-pressure-levels',
        {

            'product_type':'reanalysis',
            'area'    : '78/26/26/45', # North, West, South, East. Default: global
            'grid'    : '0.25/0.25', # Latitude/longitude grid: east-west (longitude) and north-south resolution (latitude). Default: reduced Gaussian grid
            'format':'netcdf',
            'pressure_level':level,
            'variable':var,
            'year':years_subset,
            'month':[
                '05','06',
                '07','08','09',
                
            ],
            'day':[
                '01','02','03',
                '04','05','06',
                '07','08','09',
                '10','11','12',
                '13','14','15',
                '16','17','18',
                '19','20','21',
                '22','23','24',
                '25','26','27',
                '28','29','30',
                '31'
            ],
            'time':[
                '00:00','01:00','02:00',
                '03:00','04:00','05:00',
                '06:00','07:00','08:00',
                '09:00','10:00','11:00',
                '12:00','13:00','14:00',
                '15:00','16:00','17:00',
                '18:00','19:00','20:00',
                '21:00','22:00','23:00'
            ]
        },
        filename)


if __name__ == "__main__":
	variables_single_layer = ['2m_temperature']
	years = 	['1981','1982','1983','1984','1985',  
		         '1986','1987','1988','1989','1990',
		         '1991','1992','1993','1994','1995',
		         '1996','1997','1998','1999','2000',
			 '2001','2002','2003','2004','2005',
			 '2006','2007','2008','2009','2010',
		         '2011','2012','2013','2014','2015', 
			 '2016', '2017', '2018']

	size_ = len(years) 
	splits = 2
	split_size = int(size_/splits)

	for var in variables_single_layer:
		for i in range(split_size):
			if i == split_size -1:
				download_single_layer_file(var, years[i :])
			else:
			    print(i, i+splits)
			    download_single_layer_file(var, years[i: i+split_size])
		
		

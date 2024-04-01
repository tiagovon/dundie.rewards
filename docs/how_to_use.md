# How to use


## Load data

Having a file people.csv with the following format:

csv
Jim Halpert, Sales, Salesman, jim@dundlermifflin.com
Dwight Schrute, Sales, Manager, schrute@dundlermifflin.com
Gabe Lewis, Director, Manager, glewis@dundlermifflin.com


Run dundie load command

py
dundie load people.csv


## Viewing data

### Viewing all information

bash
$ dundie show
                                        Report
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ name           ┃ dept     ┃ role     ┃ email           ┃ balance ┃ last_movement   ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ Jim Halpert    │ Sales    │ Salesman │ jim@dundlermif… │ 3000    │ 2022-03-15T13:… │
│ Dwight Schrute │ Sales    │ Manager  │ schrute@dundle… │ 2400    │ 2022-03-15T13:… │
│ Gabe Lewis     │ Director │ Manager  │ glewis@dundler… │ 500     │ 2022-03-15T13:… │
└────────────────┴──────────┴──────────┴─────────────────┴─────────┴─────────────────┘


### Filtering

Available filters are --dept and --email

bash
dundie show --dept=Sales
                                        Report
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ name           ┃ dept  ┃ role     ┃ email            ┃ balance ┃ last_movement     ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ Jim Halpert    │ Sales │ Salesman │ jim@dundlermiff… │ 3000    │ 2022-03-15T13:44… │
│ Dwight Schrute │ Sales │ Manager  │ schrute@dundler… │ 2400    │ 2022-03-15T13:43… │
└────────────────┴───────┴──────────┴──────────────────┴─────────┴───────────────────┘


> *NOTE* passing
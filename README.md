# myCrytoCoinChart


## To-do:
* [x] Parse data from remitano wesite
	* [x] Regex pattern

* [x] Database to store data
	* [x] mySQLite (Grafana does not support)
	* [ ] postgres (psycopg2)

* [ ] Display data
	* [ ] Grafana

## Implementation:
![data/flow01.png](data/flow01.png)
 

## Note:
* re pattern
	
		'''"vn"\s*:\s*(\{\s*"currency"\s*:\s*"VND"\s*,\
			\s*"btc_bid"\s*:([0-9]*[.])?[0-9]+\s*,\s*"btc_ask"\s*:([0-9]*[.])?[0-9]+\s*,\
			\s*"eth_bid"\s*:([0-9]*[.])?[0-9]+\s*,\s*"eth_ask"\s*:([0-9]*[.])?[0-9]+\s*,\
			\s*"usdt_bid"\s*:([0-9]*[.])?[0-9]+\s*,\s*"usdt_ask"\s*:([0-9]*[.])?[0-9]+\s*\})'''
* tmux 
	
		tmux
		crtl+b then d to leave/detach tmux
		crtl+b then $ to name session
		tmux attach -t session_name
		tmux list-session	to list all session
		tmux kill-session -t session_name
		tmux a attach last session

* postgres
		
		docker exec -ti -u prosgres container_name bash
		postgres -V
		psql postgres
		\du	#list user
		\q # quits
		CREATE ROLE username WITH LOGIN PASSWORD 'quoted password'
		CREATE DATABASE databasename;
		psql postgres -U patrick
		You’ll notice the prompt is slightly different – the # has changed to a >. This indicates you’re no longer using a Super User account.
		grant all privileges on database <dbname> to <username> ;

*adminer
		default user:postgres


## Tutorial:
* Tutorial 1

	https://www.sitepoint.com/getting-started-sqlite3-basic-commands/

	http://stackabuse.com/a-sqlite-tutorial-with-python/

	https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
	https://pythonspot.com/python-database-postgresql/
	https://medium.com/@beld_pro/quick-tip-creating-a-postgresql-container-with-default-user-and-password-8bb2adb82342

	https://www.cybertec-postgresql.com/en/announcing-pgwatch2-a-simple-but-versatile-postgresql-monitoring-tool/


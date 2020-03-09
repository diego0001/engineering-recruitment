# engineering-recruitment

Your assignment is to create a simple backend application with a route and a sql database. The basic tools have been provided with this repository. Clone this repository and create a branch named after yourself. Once you have completed what you can push the branch back into the repo. 

### Task:

Create a full stack (v.4.4) web application with just one route : /reptrak
Your route should return a json payload to the requester. The route must read numbers from 1 to 100 provided by a local database(*) (can be a mysql, sqlite or postgres), and process the numbers under these rules:

* If the number is multiple of 3 , print Rep.
* If the number is multiple of 5, print trak.
* If the number is multiple of 3 and multiple of 5 , print reptrak.
* Otherwise just print the number.

##### Example:
1 - 2 - Rep - 4 - Trak - Rep - 7 - 8....14 - Reptrak - 16 - 17


Database: Generate a table with entry numbers from 1 to 100. Store your sql scripts in the ./sql_scripts directory.

### Scoring

Points are weighted based on engineering methods and code efficiency. Additional points will be awarded based on:
* Knowledge of containerization
* Configuration management of dynamic environments
* 

### Database Options
##### MySQL
```bash
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:latest
```
... where `some-mysql` is the name you want to assign to your container, `my-secret-pw` is the password to be set for the MySQL root user.

###### PostgreSQL
```bash
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```
... where `some-postgres` is the name you want to assign to your container, `mysecretpassword` is the password to be set for the `postgres` root user.

TODO
Example docker run commands



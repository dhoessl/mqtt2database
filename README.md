# mqtt2database

Consists of Controller and Client.

# Controller
The Controller is handling updating the database entries for persistent storage of soundcraft ui16 config values.

In this case not every Consumer is in need to open a HTTP Connection to the Soundcraft UI16 to listen for config changes and can request specific values at anytime without letting the Soundcraft UI16 dump its whole config everytime which also takes a good amount of time to request and parse.

## Start the controller

The controller can be started as own blocking Thread if given `True` as argument on object creation. Otherwise it will run without blocking the current thread.

```
from mqtt2database import DatabaseMqttController
controller = DatabaseMqttController()
blocking_controller = DatabaseMqttController(True)
controller.start()
blocking_controller.start()  # blocks further run till its stopped
```

# Listener

The Listener can request configuration all Database data from Controller with predefined functions. It will send a message with content `dbreq` to the topic it listens to and handels the answer on the same topic. This way a request for information will be handeled by every Listener connected to the topic.

```
from mqtt2database import DatabaseMqttListener
listener = DatabaseMqttListener()
listener.req_master_update()
```

Example Coms:
```
In [3]: 2026-04-01 13:10:38 | DEBUG    | mqtt2database.core.listener:_on_message:35 - Unsolved: database/master => dbreq
2026-04-01 13:10:38 | DEBUG    | mqtt2database.core.controller:_on_message:51 - Handling Request. Topic database/master => dbreq
2026-04-01 13:10:38 | WARNING  | mqtt2database.core.listener:master_update:46 - Please set a master_update(msg) function
2026-04-01 13:10:38 | DEBUG    | mqtt2database.core.listener:_on_message:33 - Updating: database/master => 0
2026-04-01 13:10:38 | DEBUG    | mqtt2database.core.controller:_on_message:53 - Unsolved msg: database/master => 0
```

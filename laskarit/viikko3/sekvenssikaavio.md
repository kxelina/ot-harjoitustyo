```mermaid
sequenceDiagram
    participant m as main 
    participant ma as machine
    m->>ma: self._engine.start()
    participant e as engine
    ma->>e: self._fuel_tank.consume(5)
    participant f as fueltank:
    e->>f: self.fuel_contents - amount
    f-->>-m: 35
    m->>e: running
    e-->>-m: 35>0
    m-->>e: self._fuel_tank.consume(10)
    e->>f: self.fuel_contents - amount
    f-->>-m: 25
```



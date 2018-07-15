# The Network Layer (Week 2)

## The Network Layer

* Remember, on a local area network (LAN), computers communicate with one another through their MAC addresses, which is great for small scale networks.
* MAC addresses, however, don't scale well; every device on the planet has a MAC address, and there is no way to fully know where a particular device is on the planet given just its MAC address.
* The Network Layer is the solution to the problem involving internetwork transmissions.

### IP Addresses

* __IP Addresses__ are a 32-bit number made up of four octets, with each of these octets usually being described in decimal number. An example

|IP Address (Decimal): |172|16|254|1|
|-|-|-|-|-|
|IP Address (Octet): |10101100|00010000|11111110|00000001|

* Each octet must correspond to a number between 0 and 255. This means that 12.34.56.78 would be a valid IP address, but 123.456.789.100 is not a valid IP address because "456" and "789" are larger than what can be represented by the 8 bit octet.
* The decimal format (i.e. 192.168.0.1) is known as __dotted decimal notation__.
* IP Addresses are distributed by large "de facto" organizations, as opposed by being determined by hardware vendors.
    * As a result, IP addresses are better for sending and recieving data over an (or the) internet.
* IP addresses belong to networks, not to the devices attached to those networks.
    * You laptop will always have the same MAC address, but a different IP address when you sign on to different networks.
    * The LAN is responsible for assigning IP addresses to devices
    
* Through a protocol called __Dynamic Host Configuration Protocol__, a dynamic IP address is assigned to the host.
* It's also possible to manually assign a __static IP address__.
* In most cases static IP addresses are reserved for servers and network devices, while dynamic IP addresses are reserved for clients.    

### IP Datagrams and Encapsulation

* An __IP datagram__ is a highly structured series of fields that are strictly defined, like an Ethernet frame

![IP datagram](../assets/course2_ipdatagram.png)

## Subnetting

## Routing


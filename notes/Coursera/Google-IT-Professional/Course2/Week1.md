# Introduction to Networking (Week 1)

## Introduction to Computer Networking

* __Protocol:__ a defined set of standards that computers must follow in order to communicate properly.
* __Computer networking:__ the name we've given to the full scope of how computers communicate with each other.
* This course deals mainly with the _TCP/IP model_, though briefly discusses the OSI model.

## The TCP/IP Five-Layer Network Model

### Contents of the TCP/IP Five-Layer Model

||Layer Name|Protocols|Protocol Data Unit|Addressing|Analogy|
|-|---------|---------|------------------|----------|-------|
|5|Application|HTTP,SMTP,etc...|Messages|n/a|Contents of the Package|
|4|Transport|TCP/UDP|Segment|Port Numbers|Instructions for "knocking on door"|
|3|Network|IP|Datagram|IP Address|Identifies the route|
|2|Data Link|Ethernet, Wi-Fi|Frames|MAC Address|Intersections for Delivery Trucks|
|1|Physical|10 Base T, 802.11|Bits|n/a|Delivery Truck & Roads|

* The __Physical Layer__ represents the physical devices that interconnect computers.
    * Think cables, connectors, and sending signals
* The __Data Link Layer__ is responsible for defining a common way of interpreting these signals so network devices can communicate.
    * Sometimes called "Network Interface" or "Network Access Layer"
    * Here, the first protocols are introduced. (Like Ethernet)
    * __Ethernet__ standards define a protocol responsible for getting data to nodes on the same network or link.
* The __Network Layer__ allows different networks to communicate with each other through devices called "routers"
    * Sometimes called the "internet layer"
    * An __"internetwork"__ is a collection of networks connected together through routers, the most famous of these bein the __Internet__.
    * "Internet Protocol" or "IP" is the most common protocol used at the network layer; it is the "heart" of the Internet and most smaller (inter)networks around the world.
    * Network software usually follow a "client" and "server" model.
    * Client application initiates a request for data, and server applications respond with it.
* It's possible for web browsers and email clients to run at the same instance; likewise, it is possible for web and mail services to run on the same server.
* The __Transport Layer__ sorts out which client and server programs are supposed to get that data.
    * __Transmission Control Protocol (TCP)__ and __User Datagram Protocol (UDP)__ are two examples.
    * The major difference between TCP and UDP is that TCP allows for reliable data transferring while UDP does not.
* The __Application Layer__ are application specific (like those that allow for browsing the web or sending and receiving emails)

### The OSI Model \(after [Wikipedia](https://en.wikipedia.org/wiki/OSI_model)\)

|||Layer|Protocol Data Unit|Function|
|-|-|---|------------------|--------|
|7|Host Layer|Application|Data|High-level APIs, including resource sharing, remote file access|
|6|Host Layer|Presentation|Data|Translation of data between a networking service and an application; including character encoding, data compression and encryption/decryption|
|5|Host Layer|Session|Data|Managing communication sessions, i.e. continuous exchange of information in the form of multiple back-and-forth transmissions between two nodes|
|4|Host Layer|Transport|Segment, Diagram|Reliable transmission of data segments between points on a network, including segmentation, acknowledgement and multiplexing|
|3|Media Layer|Network|Packet|Structuring and managing a multi-node network, including addressing, routing and traffic control|
|2|Media Layer|Data link|Frame|Reliable transmission of data frames between two nodes connected by a physical layer|
|1|Media Layer|Physical|Symbol|Transmission and reception of raw bit streams over a physical medium|

## The Basics of Networking Devices

### Cables

* __Cables__ are what connect different devices to each other, allowing data to be transmitted over them
    * Cables can be split into two categories: copper and fibre
    * __Copper__ cables are the most common kind of networking cables, they are made up of multiple pairs of copper wires inside plastic insulators. Copper wires send data by changing the voltage between two ranges. The "recieving end" can then recieve these voltages and interpret them as 0's and 1's which can be translate into different kinds of data.
        * The most common forms of copper twisted-pair cables used in networking are __Cat5__ (older), __Cat5e__ and __Cat6__ cables. "Cat" is a shorthand for "category". Different categories have different physical characteristics.
        * How the copper wire is twisted can make a huge difference in the transmission rate of data, and how resistant they are to outside interference.
    * __Crosstalk__ is what happens when an electric pulse on one wire is accidentally detected on another wire.
        * As a result, the "recieving end" is unable to recieve the data, resulting in error.
    * Cat5e cables are made in a way that makes it less likely that data needs to be retransmitted. More data can be transferred in a small amount of time.
    * Cat6 cables are even more strict in their specifications to avoid crosstalk. Cat6 cables can transmit more data at a faster rate than Cat53, but are shorter as a trade-off for speed and reliability.
    * __Fibre optic cables__ are the second category of cables, which contain individual optical fibres, which are tiny tubes made out of glass, with the width the size of a human hair. They transport beams of light, using pulses of light to represent 0's and 1's, and can even resist electromagnetic interference. The only drawback is that they're more fragile and expensive.
        * As an added bonus, fibre wires can transfer data at longer distances than copper!    

* You are more likely to run into fibre wires in a data centre, and run into copper wires at small homes.

### Hubs and Switches

* A __collision domain__ is a network segment where only one device can communicate at a time; if multiple systems try sending data at the same time, the electrical pulses sent across the cable can intefere with each other.

* Point-to-point network connects can be useful in some settings, but we need to connect multiple computers at the same instance. That's where hubs and switches comes in.
    * A __hub__ is a physical layer device that allows for connections from many computers at once. Hubs are rare because they rely on a collision domain, which is undesirable.
    * A __network switch__ is similar to a hub, but rather than operating on the "physical", "layer 1" part of the network, it operates on the "data link", "layer 2" part of the network, meaning that it can inspect the contents of the Ethernet protocol data, and work out where data should be sent to. This almost eliminates collision domains.
    
* Hubs and switches are the primary devices used to connect computers on a single network, usually refered to a __LAN__ or __local area network__.

### Routers

* A __router__ is a device that knows how to forward data between independent networks
    * Routers operate on layer 3, the "network" part of the TCP/IP Five-Layer Model.
    * Routers inspect IP data to determine where to send content.
* ISP = Internet Service Provider
* The __Border Gateway Protocol__ is what allows routers to share data with each other. It lets them learn about the most optimal paths to forward traffic.

### Servers and Clients

* __Nodes__ refer to the devices on the network (laptop, desktop smartphone, IOT device, etc.)
* A __client__ is something that requests data whilst a __server__ is something that responds with data.
* Nodes can act as both clients and servers at some capacity
    * i.e. an node that's primary purpose is to act as an email server may occationally make DNS requests or a desktop server can occationally respond with data.

## The Physical Layer

## The Data Link Layer

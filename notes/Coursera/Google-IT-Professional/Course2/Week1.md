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

## The Physical Layer

## The Data Link Layer

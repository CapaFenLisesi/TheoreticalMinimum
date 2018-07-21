# Networking Services (Week 4)

## Name Resolution

### Why do we need DNS?

* __Domain Name System (DNS)__ is a global and highly distributed network service that resolves strings of letters into IP addresses for you
* A __Domain Name__ is the term we use for something that can be resolved by DNS
* DNS is useful because it allows us to only have to memorise domain names instead of IP addresses
    * They're also useful in the event that the IP address of the service changes, the domain name can just be reconfigured to "point" to the new IP address
    * DNS also allows us to distribute web servers across the globe, so that users can access services quicker by geographical location
    
### The Many Steps of Name Resolution

* __Time to Live (TTL):__ is a value, in seconds, that can be configured by the owner of a domain name for how long a name server is allowed to cache an entry before it should discard it and perform a full resolution again
* __Anycast__ is a technique that's used to route traffic to different destinations depending on factors like location, congestion, or link health

* There are five primary types of DNS Servers:
    1. __Caching name servers__ - purpose is to store known domain name lookups for a certain amount of time, stores them in cache
    2. __Recursive name servers__ - purpose is to store known domain name lookups for a certain amount of time, this one specifically performs full DNS resolution requests
    3. __Root name servers__ - these are 13 authorative name servers that redirects DNS requests to the appopriate TLD name server
    4. __TLD name servers__ - name servers that redirect to .com, .org, .net, .edu, .gov, .horse, etc.
    5. __Authoritative name servers__ these are the DNS servers that hold the records for a particular domain name
    
* DNS works like this:
    1. The User makes a DNS request to the Caching/Recursive Name server
    2. If the domain name is not cached in the DNS server, then forward the request to one of the 13 root servers and get a TLD server, the caching/recursive server will then request information from a TLD name server, and finally will request information from the name server in charge of the domain name.

### DNS and UDP

* Remember that UDP is connectionless, ergo data can be transmitted quicker
* A single DNS request and response can fit inside a single datagram
* With UDP, DNS requests and responses go from an average of 44 datagram transfers to eight datagram transfers
* It should be noted that there are DNS implementations that use TCP

## Name Resolution in Practice

## Dynamic Host Configuration Protocol

## Network Address Translation

## VPNs and Proxies

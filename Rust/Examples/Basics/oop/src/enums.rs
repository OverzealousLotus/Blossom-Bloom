// Sometimes in Rust, there isn't a data type that fits our needs.
// Why not create our own?

// Suppose we want to collect proxies from a website.
// Let's create a data type: IpAddr, which has two variations: Ipv4 and 6.
enum IpAddr {
    Ipv4,
    Ipv6
}

// Now let's create a function to filter out all Ipv6 addresses.
fn filter(address: IpAddr) -> bool {
    match address {
        IpAddr::Ipv6 => return false,

        IpAddr::Ipv4 => return true
    }
}


fn main() {
    let addr_one: IpAddr = IpAddr::Ipv4;
    let addr_two: IpAddr = IpAddr::Ipv6;
    let addr_three: IpAddr = IpAddr::Ipv6;

    println!("First address is {}", filter(addr_one));
    println!("Second address is {}", filter(addr_two));
    println!("Third address is {}", filter(addr_three));
}
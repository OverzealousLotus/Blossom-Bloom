// Unlike most other languages, Rust does not have Classes.
// Thus, we must create our own class structure.
// To start, we have Structs, which bring similar pieces of data together.

// Below, I define a Struct called Human.
// Humans can have names, have ages, and attributes.
struct Human {
    name: String,
    age: u8,
    smart: bool,
}

// Alternatively, we can create a Tuple Struct.
// Tuple Structs behave similarly to normal Structs
// -except their fields have no name hence them being Tuples.
#[derive(Debug)] // Ignore
struct Pizza(String, String, String);

// Lastly, Unit Structs. These Structs have no/one value. ( Just like a Unit Tuple.)
#[derive(Debug)] // Ignore
struct Tasty;


fn main() {
    // Now we can create an instance of a Human.
    let mut lisa: Human = Human {
        name: String::from("Lisa Homing"),
        age: 16,
        smart: true
    };

    // To access attributes from "lisa", we can use .attribute
    println!("{} is {} years old!", lisa.name, lisa.age);
    println!("The rumours about her intelligence are {}!", lisa.smart);

    // With this method, we can also modify traits of Lisa.
    // ( Remember to make your Struct instance mutable. )

    lisa.smart = false;
    println!("Oh no! Lisa hit her head! Now the rumours are {}!", lisa.smart);

    // Let's create a pizza for Lisa.

    let meat_lovers: Pizza = Pizza(String::from("Pepperoni"), String::from("Sausage"), String::from("Bacon"));
    println!("Lisa's favorite pizza has: {meat_lovers:?}!");

    // Now is it tasty?

    let status: Tasty = Tasty;
    println!("She thinks it's {status:?}");
}
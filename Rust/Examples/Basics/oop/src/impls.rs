// If you've ever used any other programming language, you will know what Methods are.
// Otherwise, Methods are functions inside of Classes, or in Rust's case, Structs.
// These are functions associated with a given Class, or Struct.
// To add Methods to Structs, we use the "impl" keyword.

struct Bird {
    name: String,
    speed: String,
    chirping: bool
}

// Let's implement a way to fetch our bird's name and speed!
// While we're at it, we can also make it chirp!
impl Bird {
    // "&self or self" refers to our bird itself.
    // At the moment, we do not know what it will be called.
    // Thus, self acts a placeholder to access our bird.
    fn get_name(&self) -> String {
        return self.name.clone(); // We must clone() Strings, as they cannot be copied.
    }

    fn get_speed(&self) -> String {
        return self.speed.clone();
    }

    fn chirp(&self) -> () {
        if self.chirping {
            println!("{} is chirping in the sunlight!", self.get_name());
        } else {
            println!("All is quiet in the Commonweath.");
        }
    }

}

fn main() {
    // First, let's instantiate our Bird.
    let toucan: Bird = Bird {
        name: String::from("Richard"),
        speed: String::from("Fast"),
        chirping: true
    };

    // Now chirp!
    toucan.chirp();
    println!("{} is {} for a toucan!", toucan.get_name(), toucan.get_speed());
}
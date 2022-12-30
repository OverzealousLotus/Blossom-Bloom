// Let's say we create a few similar Structs in Rust:

struct Feline {
    name: String,
    age: u8,
    agility: u8,
    furry: bool
}

struct Bolvine {
    name: String,
    age: u8,
    agility: u8,
    furry: bool,
    milked: bool
}

// What if we want to add Methods to these structs? We'll have to redefine already defined functions.
// This is not the Programmer way. This is where Rust Traits come in. Traits allow us to reuse-
// -already defined functions, and provide a connection between similar Structs.

trait Animal {
    // new() allows us to create a Struct with shorthand syntax.
    // For example, String::new() does this, along with Box::new()
    fn new(name: String, age: u8, agility: u8, furry: bool) -> Self;

    fn name(&self) -> String;

    fn age(&self) -> u8;

    fn agility(&self) -> u8;

    fn fur(&self) -> bool;
    // You'll notice all of this syntax seems, familiar, except they're missing a body.
    // This is because Traits allow us to define the body while implementing them for each Struct.
}

// How do we implement our Animal Trait? With "impl" and "for", of course.

impl Animal for Feline {
    // Remember the new() function returning Self? Self is Feline in this case.
    fn new(name: String, age: u8, agility: u8, furry: bool) -> Feline {
        return Feline {name: name, age: age, agility: agility, furry: furry}
    }

    // Now the syntax returns to an expected state.
    fn name(&self) -> String {
        return self.name.clone();
    }

    fn age(&self) -> u8 {
        return self.age;
    }

    fn agility(&self) -> u8 {
        return self.agility
    }

    fn fur(&self) -> bool {
        return self.furry
    }
}

impl Animal for Bolvine {
    // Remember the new() function returning Self? Self is Feline in this case.
    // Since milked is not a default trait for Animal, we have to set it to false.
    fn new(name: String, age: u8, agility: u8, furry: bool) -> Bolvine {
        return Bolvine {name: name, age: age, agility: agility, furry: furry, milked: false}
    }

    // Now the syntax returns to an expected state.
    fn name(&self) -> String {
        return self.name.clone();
    }

    fn age(&self) -> u8 {
        return self.age;
    }

    fn agility(&self) -> u8 {
        return self.agility
    }

    fn fur(&self) -> bool {
        return self.furry
    }
}
// Now, let's stray away from our Bolvine Animal friend.

impl Feline {
    fn meow(&self) -> () {
        println!("{} is meowing cutely!", self.name);
    }
}

impl Bolvine {
    fn milk(&mut self) -> () {
        if self.milked {
            println!("Oh no! {} kicked because they're out of milk!", self.name);
        } else {
            println!("{} has been successfully milked!", self.name);
            self.milked = true;
        }
    }
}
fn main() {
    // Time to instantiate our Structs, except now, we can use the new() function we created.
    let mut garet: Bolvine = Bolvine::new(String::from("Garet"), 6, 25, false);
    let isaac: Feline = Feline::new(String::from("Isaac"), 3, 45, true);

    // Lastly, let's milk garet and make isaac meow.
    garet.milk();
    isaac.meow();

    // Let's check to see if we can milk garet again.
    garet.milk();
}
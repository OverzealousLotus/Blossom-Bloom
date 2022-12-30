// I have no idea what the purpose of Unions are in Rust, but I'll try.
// Unions in Rust are similar to Structs, except their items are stored in the same memory space.
// Thus, when one field is given a value, any other field is overridden. Let's create one.

union Arrows {
    flame: bool,
    rime: bool,
    wind: bool
}

// Let's say we're making a video game, and our player can only have one type of arrow.
fn main() {
    let mut inventory: Arrows = Arrows {flame: true};
    // Their inventory now contains a flame arrow.
    unsafe {
        if inventory.flame == true {
            println!("Player has acquired flame arrows!");
        }
    
        // However, what if they switch to wind?

        inventory = Arrows{wind: true};

        // I DON'T GET UNIONS HELP
        if inventory.flame == true {
            println!("Player has kept flame arrows!");
        } else if inventory.wind == true {
            println!("Player has dropped flame arrows for wind arrows!");
        } else if inventory.rime == true {
            println!("Player has dropped flame arrows for rime arrows!");
        }
    }
}
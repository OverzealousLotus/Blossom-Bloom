// Sometimes, we need to expect if there is an absence of a value, or-
// -an unwanted value is present. In the Rust-Lang Book, this is the example-
// -they provide. It makes it very clear why Option<T> exists.

// Option<T> can be one of two types: Some() kind of value, or None.
// It cannot be both. Thus, Option<T> will always be something, or nothing.
fn divide(numerator: f64, denominator: f64) -> Option<f64> {
    if denominator == 0.0 {
        return None; // If the denominator is zero, then we return None
    } else {
        return Some(numerator / denominator); // if the denominator is NOT zero, then we return something.
    }
}

fn main() {
    
    let friends: Option<f64> = divide(10.0, 5.0);

    // Now we can grab the values themselves.
    match friends {
        Some(xanther) => println!("I have at least {xanther} friends!"),

        None => println!("You cannnot divide by zero! Please try again!")
    }
}
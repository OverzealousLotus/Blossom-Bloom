// Back in the day, Boxes in Rust were primarily used to allocate values to The Heap.
// However, nowadays there are way more methods to perform the same task.
// Fortunately, Boxes still have a use. Cons Lists.
// Cons Lists are recursive values that store themselves.
// There is no built-in method to create one, but we can create one ourselves.

//  enum ConsList<T> {
//      Cons(T, ConsList<T>),
//      Nil
//  }

// In this example, Rust will throw an error, stating our ConsList has infinite size.
// Why is this? Let's try to evaluate the ConsList ourself. First, we create a Cons() type.
// Then, we add a Generic Type as its first value, then itself as the second value.
// This is where the problems occur. Now we have to ask: "Where does that inner Cons() lead?"
// Now, we have an infinite loop of trying to find an end to all of these Cons() data types.
// Nil is never reached. To solve this, we use the Box<T> type. Boxes have a finite size in Rust.
// Therefore, if we wrap our inner ConsList<T> into a Box<T>, then it HAS to have an end.

#[derive(Debug)]
enum ConsList<T> {
    Cons(T, Box<ConsList<T>>),
    Nil
}


use ConsList::Cons;
use ConsList::Nil;
fn main() {
    // Now, we have our Cons List in Rust! ^^
    let storage: ConsList<u8> = Cons(10, Box::new(Cons(20, Box::new(Cons(30, Box::new(Nil))))));
    println!("{storage:?}");
}
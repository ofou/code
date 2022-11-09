# Computer

## Open-source book to master data structures, algorithms and coding interviews from first principles

<https://github.com/ofou/code/blob/d30f6ad479cd7070b7e28666f5422e7f6b8b43f9/book/hello_world.py#L1>

Inspired by books like [Code], [Nand2Tetris], the [42 School] program, [Karpathy]'s small projects, and a [hacker's curriculum], this project aims to build an understanding of the first principles in computer science by building real projects. No need for books like Cracking the Coding Interview after you read this one.

It's intended to be a physical[^1] companion to the eponymous [YouTube] series.

[Code]: https://www.charlespetzold.com/blog/2022/08/Code-2nd-Edition-Now-Available.html
[42 School]: https://42.fr/en/the-program/software-engineer-degree
[Nand2Tetris]: https://www.nand2tetris.org
[hacker's curriculum]: https://github.com/geohot/fromthetransistor
[Karpathy]: https://github.com/karpathy
[YouTube]: https://www.youtube.com/@omarnomad

[^1]: This is a work-in-progress to later turn into a proper [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) and printing it as an affordable physical book on demand.

## Data Structures

### Linked Lists

### Stack

The basic idea of a stack is that you can only access the most recently added element. A stack is a Last In First Out (LIFO) data structure. The most recently added element is always the first to be removed. Imagine a deck of cards in which you put cards on top of the deck and take cards from the top of the deck. You can only access the top card, which is the most recently added card.

In Python, a stack is implemented using a list. All the stack operations are done using list methods.

Operations on a stack are all **`O(1)`.**


- `is_empty()` - Returns `True` if the stack is empty, `False` otherwise.
- `push(item)` - Adds an item to the top of the stack. It needs the item and returns nothing.
- `pop()` - Removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
- `peek()` - Returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
- `size()` - Returns the number of items on the stack. It needs no parameters and returns an integer.

Here is a minimal implementation of the stack class:

<https://github.com/ofou/code/blob/main/data_structures/stack/stack.py#L1-L27>

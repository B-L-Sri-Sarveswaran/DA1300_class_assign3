from typing import List


def printer_queue_order(pages):
    """
    Problem 1: Round-robin printer.

    Given the number of pages for each document (in submission order),
    simulate round-robin printing (one page at a time, front of queue
    to back of queue) and return the document indices in the order
    they finish printing.

    Args:
        pages: pages[i] is the number of pages in document i.

    Returns:
        List of document numbers in the order they finish printing.
    """
    out=[]
    docs=[i for i in range(len(pages))]
    while pages:
        pages[0]-=1
        if pages[0]==0:
            pages.pop(0)
            out.append(docs.pop(0))
        else:
            pages.append(pages.pop(0))
            docs.append(docs.pop(0))
    return out



if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    print(printer_queue_order([1, 1, 1]))  # expected: [0, 1, 2]

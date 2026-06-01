from multiprocessing import Process, Pipe
import os


def child_process(conn):
    # Display the child process PID
    print(f"Child [PID {os.getpid()}] waiting for data...")

    # Receive data from the parent
    message = conn.recv()

    print(f"Child [PID {os.getpid()}] received: {message}")

    # Transform the message
    processed_message = message.upper()

    print(f"Child [PID {os.getpid()}] processing data...")

    # Send the result back to the parent
    conn.send(processed_message)

    conn.close()


if __name__ == "__main__":

    # Create a Pipe for communication
    parent_conn, child_conn = Pipe()

    # Create the child process
    child = Process(target=child_process, args=(child_conn,))

    print(f"Parent [PID {os.getpid()}] creating child process...")

    child.start()

    # Data to send
    message = "hello operating systems"

    print(f"Parent [PID {os.getpid()}] sending data: {message}")

    parent_conn.send(message)

    # Receive processed data
    result = parent_conn.recv()

    print(f"Parent [PID {os.getpid()}] received processed data: {result}")

    child.join()

    print(f"Parent [PID {os.getpid()}] child process finished.")

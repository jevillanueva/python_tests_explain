if __name__ == "__main__":
    assert 10 == 10
    print("Primer assert superado")
    try:
        assert 10 == 20, "Segundo assert failed"
    except AssertionError as error:
        print(error)
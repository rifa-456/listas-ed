class ExecutionError(Exception):
    """Classe base para todas as exceções."""

    pass

class Empty(ExecutionError):
    """Exceção lançada por Queue."""
    pass
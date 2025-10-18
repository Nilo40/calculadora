import customtkinter as ctk
from tkinter import messagebox


class CalculadoraApp(ctk.CTk):
    """Classe principal da calculadora."""

    def __init__(self):
        super().__init__()

        # Janela principal
        self.title("Calculadora ADS")
        self.geometry("320x460")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Campo de entrada
        self.entrada = ctk.CTkEntry(
            self, justify="right", font=("Roboto", 28), width=280, height=60
        )
        self.entrada.pack(pady=20)

        # Frame para os botões
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=10, pady=10)

        # Layout dos botões
        botoes = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["=",],
        ]

        # Criar botões dinamicamente
        for linha in botoes:
            linha_frame = ctk.CTkFrame(self.frame)
            linha_frame.pack(pady=5)
            for texto in linha:
                if texto == "=":
                    btn = ctk.CTkButton(
                        linha_frame,
                        text=texto,
                        width=260,
                        height=60,
                        corner_radius=15,
                        fg_color="#00ADB5",
                        hover_color="#009BA3",
                        font=("Roboto", 24, "bold"),
                        command=self._calcular,
                    )
                elif texto == "C":
                    btn = ctk.CTkButton(
                        linha_frame,
                        text=texto,
                        width=60,
                        height=60,
                        fg_color="#FF5722",
                        hover_color="#E64A19",
                        corner_radius=15,
                        font=("Roboto", 22, "bold"),
                        command=self._limpar,
                    )
                else:
                    btn = ctk.CTkButton(
                        linha_frame,
                        text=texto,
                        width=60,
                        height=60,
                        corner_radius=15,
                        font=("Roboto", 22),
                        command=lambda t=texto: self._adicionar_texto(t),
                    )
                btn.pack(side="left", padx=5)

    def _adicionar_texto(self, valor: str):
        """Adiciona o número ou operador na entrada."""
        self.entrada.insert("end", valor)

    def _limpar(self):
        """Limpa o campo de entrada."""
        self.entrada.delete(0, "end")

    def _calcular(self):
        """Avalia a expressão e mostra o resultado."""
        expressao = self.entrada.get()
        try:
            resultado = eval(expressao)
            self._limpar()
            self.entrada.insert("end", str(resultado))
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Divisão por zero não é permitida.")
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida.")
            self._limpar()


if __name__ == "__main__":
    app = CalculadoraApp()
    app.mainloop()

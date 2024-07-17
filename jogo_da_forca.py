import flet as ft
import string
import random

#Breakpoint      Dimension
#xs               <576px
#sm               >= 576px
#md               >= 768px
#lg               >= 992px
#xl               >= 1200px
#xxl              >= 1400px

def letter_guess(letter):
    return ft.Container(
                height=50,
                width=50,
                border_radius=ft.border_radius.all(5),
                content=ft.Text(
                    value=letter,
                    color='white',
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD
                ),
                bgcolor='orange',
            )

def main(page: ft.Page):
    
    page.bgcolor = ft.colors.BROWN_600
    page.window_title_bar_hidden = True

    avaiable_words = ['PYTHON', 'FLET', 'PROGRAMADOR']
    choiced = random.choice(avaiable_words)

    
    def validate_letter(e):
        for pos, letter in enumerate(choiced):
            if e.control.content.value == letter:
                word.controls[pos] = letter_guess(letter=letter)
                word.update()
        
        if e.control.content.value not in choiced:
            victim.data += 1

            if victim.data > 7:
                page.dialog = ft.AlertDialog(
                    title=ft.Text(value='Você perdeu! :('),
                    open=True
                )
                page.update()

            errors = victim.data
            victim.src = f'images/hangman_{errors}.png'
            victim.update()
        
        e.control.disabled = True
        e.control.gradient = ft.LinearGradient(colors=['grey'])
        e.control.update()
    
    
    victim = ft.Image(
        data = 0,
        src='images/hangman_0.png',
        repeat = ft.ImageRepeat.NO_REPEAT,
        height=300
    )


    word = ft.Row(
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            letter_guess('_') for letter in choiced
        ]
    )

    game = ft.Container(
        col={'xs':12, 'lg': 6},
        padding=ft.padding.all(50),
        
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                victim,
                word
            ],
        )
    )
    
    scene = ft.Image(col=12, src='images/scene.png')

    keyboard = ft.Container(
        col={'xs': 12, 'lg': 6},
        image_src='images/keyboard.png',
        image_repeat=ft.ImageRepeat.NO_REPEAT,
        image_fit= ft.ImageFit.FILL,
        padding=ft.padding.only(top=150, left=80, right=80, bottom=50),
        content=ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    on_click=validate_letter,
                    height=50,
                    width=50,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value=letter,
                        color='white',
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD
                    ),
                    #bgcolor='orange',
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=['amber', ft.colors.DEEP_ORANGE],
                    )
                ) for letter in string.ascii_uppercase
            ]
        )
    )

    layout = ft.ResponsiveRow(
        expand=True,
        columns=12,
        controls=[
            scene,
            game,
            keyboard,
            scene,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(layout)


if __name__=='__main__':
    ft.app(target=main, assets_dir="assets")
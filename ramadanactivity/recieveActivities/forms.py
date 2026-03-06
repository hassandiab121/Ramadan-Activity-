from django import forms


class ActivityForm(forms.Form):
    name = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'أدخل اسم النشاط',
            }
        ),
        label='اسم النشاط',
        required=True,
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-textarea',
                'placeholder': 'أدخل وصف النشاط',
            }
        ),
        label='الوصف',
        required=False,
    )

    location = forms.CharField(
        max_length=300,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'أدخل موقع النشاط (مثال: المسجد، الحي،...)',
            }
        ),
        label='الموقع',
        required=True,
    )

    day = forms.ChoiceField(
        choices=[(i, f'{i} رمضان') for i in range(1, 31)],
        label='التاريخ',
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            }
        ),
    )


class JoinActivityForm(forms.Form):
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'أدخل رقم واتساب مكون من 11 رقماً',
                'type': 'tel',
                'inputmode': 'numeric',
            }
        ),
        label='رقم واتساب',
        required=True,
    )

    def clean_phone(self):
        raw = self.cleaned_data.get('phone', '')
        # Keep only digits
        digits = ''.join(ch for ch in raw if ch.isdigit())
        if len(digits) != 11:
            raise forms.ValidationError('رقم الجوال يجب أن يحتوي على 11 رقمًا بالضبط.')
        return digits


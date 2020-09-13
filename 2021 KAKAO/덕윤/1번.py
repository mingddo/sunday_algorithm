def solution(new_id):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char = '-_.'
    number = '0123456789'
    # 1단계 : 소문자로 바꾸어주기.
    m_id1 = new_id.lower()
    # 2단계 : 알파벳 및 특수문자 제거해주기
    m_id2 = ''
    m_id3 = ''
    m_id4 = ''
    m_id5 = ''
    for m1 in m_id1:
        if m1 in alphabet or m1 in char or m1 in number:
            m_id2 += m1
    # 3단계 : 마침표 2개 이상 연속되면 1개로 치환하기
    for i in range(len(m_id2)):
        if i == 0:
            m_id3 += m_id2[i]
        elif m_id2[i] == '.' and m_id3[-1] =='.':
            continue
        else:
            m_id3 += m_id2[i]
    # 4단계 : 앞 뒤 마침표 제거해주기
    if m_id3[0] == '.':
        m_id4 = m_id3[1:]
    elif m_id3[-1] == '.':
        m_id4 = m_id3[:-1]
    else:
        m_id4 = m_id3[:]
    # 5단계 : 빈문자열이면 a를 대입
    if m_id4 == '':
        m_id4 += 'a'
    # 6단계: 16자 이상이면 15까지만
    if len(m_id4) >= 16:
        m_id5 = m_id4[:15]
    else:
        m_id5 = m_id4[:]
    # 앞 뒤 마침표 제거해주기
    if m_id5[0] == '.':
        m_id5 = m_id5[1:]
    elif m_id5[-1] == '.':
        m_id5 = m_id5[:-1]

    # 7단계 : 2자 이하라면 3자 이상이 될 때 까지 마지막 글자 반복해서 쓰기
    if 0<= len(m_id5) <=2:
        last = m_id5[-1]
        while len(m_id5) < 3:
            m_id5 += last
        answer = m_id5
    else:
        answer = m_id5
    return answer

r = solution("123_.def")
print(r)
# def solution("z-+.^.")
# def solution("=.=")
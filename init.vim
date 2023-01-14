" Plugins
call plug#begin('~/.local/share/nvim/plugged')
Plug 'preservim/nerdtree'
Plug 'junegunn/fzf', {'do': { -> fzf#install() } } 
Plug 'numkil/ag.nvim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
Plug 'github/copilot.vim'
Plug 'morhetz/gruvbox'
Plug 'vim-scripts/loremipsum'
Plug 'mitsuhiko/vim-jinja'
call plug#end()
autocmd vimenter * ++nested colorscheme gruvbox
" Open NERDTree if opened on a directory
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" Slightly wider than default :let g:NERDTreeWinSize=50 <leader>-f opens the file's directory in NERDTree
nmap <leader>f :NERDTreeFind<CR>

" Split navigation
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
set splitbelow
set splitright
nnoremap _ :sp<return>

" lorem 
nnoremap <leader>t :Loremipsum<Space>

" Fuzzy finder using C-p
nnoremap <C-p> :FZF<CR>

syntax on

" Transparent bottom bar
hi StatusLine ctermbg=NONE cterm=bold

" Disable autocomment for new lines
autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" Relative numbers are nice
set number

au BufReadPost *.jinja2 set syntax=htmljinja

" Metals stuff

set hidden
set nobackup
set nowritebackup
set updatetime=300

nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

set clipboard+=unnamedplus

" Formatting popup menu
" TODO how to change foreground color?
hi Pmenu ctermbg=60 guibg=60

" Stop with the grey already
hi SignColumn ctermbg=NONE guibg=NONE

" K for show documentation
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if &filetype == 'vim'
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

" <leader>c clears highlighting from searches because I'm getting irritated about how much I type this command
nmap <leader>c :noh<CR>


" <leader>l toggles no numbers -> absolute numbers -> relative numbers
nnoremap <leader>l :let [&nu, &rnu] = [&nu+&rnu==0,&nu]<CR>

" <leader>h toggles hex edit mode
nnoremap <leader>h :call HexEditToggle()<CR>

let g:hex_mode = 0

function! HexEditToggle()
    if g:hex_mode
        :%!xxd -r
        let g:hex_mode = 0
    else
        :%!xxd
        let g:hex_mode = 1
    endif
endfunction


"""""""" Indentation

" 2 spaces by default
set tabstop=4
set shiftwidth=2
set softtabstop=2
set expandtab
set smarttab

" Match go fmt style
autocmd FileType go setlocal tabstop=4 shiftwidth=4 softtabstop=0 noexpandtab

